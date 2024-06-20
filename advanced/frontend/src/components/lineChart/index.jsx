import { useEffect, useRef } from 'react';
import * as d3 from 'd3';
import './lineChart.css';

const LineChart = ({ data }) => {
    const svgRef = useRef();

    useEffect(() => {
        const svg = d3.select(svgRef.current);
        const { width, height } = svg.node().getBoundingClientRect();
        const margin = { top: 20, right: 20, bottom: 50, left: 50 };
        const innerWidth = width - margin.left - margin.right;
        const innerHeight = height - margin.top - margin.bottom;

        svg.selectAll('*').remove();

        const x = d3.scaleTime().range([0, innerWidth]);
        const y = d3.scaleLinear().range([innerHeight, 0]);

        const color = d3.scaleOrdinal(d3.schemeCategory10);

        const line = d3.line()
        .x(d => x(new Date(d.date)))
        .y(d => y(d.total_amount));

        const g = svg.append('g').attr('transform', `translate(${margin.left},${margin.top})`);

        const types = Array.from(new Set(data.map(d => d.type_name)));

        x.domain(d3.extent(data, d => new Date(d.date)));
        y.domain([0, d3.max(data, d => d.total_amount)]);

        color.domain(types);

        g.append('g')
        .attr('transform', `translate(0,${innerHeight})`)
        .call(d3.axisBottom(x).tickFormat(d3.timeFormat("%b %d")).ticks(d3.timeDay.every(1)))
        .selectAll("text")
        .style("text-anchor", "end")
        .attr("dx", "-0.8em")
        .attr("dy", "0.15em")
        .attr("transform", "rotate(-65)");

        g.append('g')
        .call(d3.axisLeft(y));

        const typeData = types.map(type => ({
        type,
        values: data.filter(d => d.type_name === type)
        }));

        const type = g.selectAll('.type')
        .data(typeData)
        .enter().append('g')
        .attr('class', 'type');

        type.append('path')
        .attr('class', 'line')
        .attr('d', d => line(d.values))
        .style('stroke', d => color(d.type));

        // Adding legend
        const legend = svg.append('g')
        .attr('class', 'legend')
        .attr('transform', `translate(${innerWidth - 20}, 20)`);

        legend.selectAll('rect')
        .data(types)
        .enter()
        .append('rect')
        .attr('x', 0)
        .attr('y', (d, i) => i * 20)
        .attr('width', 10)
        .attr('height', 10)
        .style('fill', d => color(d));

        legend.selectAll('text')
        .data(types)
        .enter()
        .append('text')
        .attr('x', 20)
        .attr('y', (d, i) => i * 20 + 9)
        .text(d => d)
        .style('font', '10px sans-serif');

    }, [data]);

    return (
        <svg ref={svgRef} style={{ width: '100%', height: '500px' }}></svg>
    );
};

export default LineChart;
