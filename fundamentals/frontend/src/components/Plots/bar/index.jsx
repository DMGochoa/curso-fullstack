import React, { useEffect, useRef } from 'react';
import * as d3 from 'd3';

const BarChart = ({ data }) => {
  const svgRef = useRef();

  useEffect(() => {
    // Configuración del gráfico
    const margin = { top: 20, right: 30, bottom: 40, left: 50 };
    const width = 300 - margin.left - margin.right;
    const height = 400 - margin.top - margin.bottom;

    // Crear el contenedor SVG
    const svg = d3.select(svgRef.current)
      .attr('width', width + margin.left + margin.right)
      .attr('height', height + margin.top + margin.bottom)
      .append('g')
      .attr('transform', `translate(${margin.left},${margin.top})`);

    // Escalas
    const x = d3.scaleBand()
      .domain(data.map(d => d.type))
      .range([0, width])
      .padding(0.1);

    const y = d3.scaleLinear()
      .domain([0, d3.max(data, d => d.average_monthly_amount)])
      .range([height, 0]);

    // Ejes
    const xAxis = d3.axisBottom(x);
    const yAxis = d3.axisLeft(y);

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

    // Añadir las barras
    svg.selectAll('.bar')
      .data(data)
      .enter()
      .append('rect')
      .attr('class', 'bar')
      .attr('x', d => x(d.type))
      .attr('y', d => y(d.average_monthly_amount))
      .attr('width', x.bandwidth())
      .attr('height', d => height - y(d.average_monthly_amount))
      .attr('fill', 'steelblue');

  }, [data]);

  return (
    <svg ref={svgRef}></svg>
  );
};

export default BarChart;
