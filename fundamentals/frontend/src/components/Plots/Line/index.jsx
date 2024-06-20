import { useEffect, useRef } from 'react';
import * as d3 from 'd3';

const LineChart = ({ data }) => {
    const svgRef = useRef();

    useEffect(() => {
        // Configuración del gráfico
        const margin = { top: 20, right: 30, bottom: 50, left: 40 };
        const width = 800 - margin.left - margin.right;
        const height = 350 - margin.top - margin.bottom;

        // Crear el contenedor SVG
        const svg = d3.select(svgRef.current)
        .attr('width', width + margin.left + margin.right)
        .attr('height', height + margin.top + margin.bottom)
        .append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);

        // Parsear las fechas
        const parseDate = d3.timeParse('%Y-%m-%d');
        data.forEach(d => {
        d.date = parseDate(d.date);
        });

        // Escalas
        const x = d3.scaleTime()
        .domain(d3.extent(data, d => d.date))
        .range([0, width]);

        const y = d3.scaleLinear()
        .domain([0, d3.max(data, d => d.total_amount)])
        .range([height, 0]);

        const color = d3.scaleOrdinal(d3.schemeCategory10);

        // Ejes
        const xAxis = d3.axisBottom(x).tickFormat(d3.timeFormat('%Y-%m-%d')).tickSize(-height);
        const yAxis = d3.axisLeft(y).tickSize(-width);

        svg.append('g')
        .attr('class', 'x-axis')
        .attr('transform', `translate(0,${height})`)
        .call(xAxis)
        .selectAll('text')
        .attr('transform', 'rotate(45)')
        .style('text-anchor', 'start');

        svg.append('g')
        .attr('class', 'y-axis')
        .call(yAxis);

        // Agrupar datos por tipo
        const types = d3.group(data, d => d.type);

        // Line generator
        const line = d3.line()
        .x(d => x(d.date))
        .y(d => y(d.total_amount));

        // Añadir las líneas
        types.forEach((values, key) => {
        svg.append('path')
            .datum(values)
            .attr('fill', 'none')
            .attr('stroke', color(key))
            .attr('stroke-width', 1.5)
            .attr('d', line);
        });

        // Añadir la leyenda
        const legend = svg.selectAll('.legend')
        .data(types.keys())
        .enter().append('g')
        .attr('class', 'legend')
        .attr('transform', (d, i) => `translate(-120,${i * 20})`);

        legend.append('rect')
        .attr('x', width + 20)
        .attr('width', 18)
        .attr('height', 18)
        .style('fill', color);

        legend.append('text')
        .attr('x', width + 45)
        .attr('y', 9)
        .attr('dy', '.35em')
        .style('font-size', '14px')
        .style('fill', 'white')
        .style('text-anchor', 'start')
        .text(d => d);
    }, [data]);

    return (
        <svg ref={svgRef}></svg>
    );
};

export default LineChart;
