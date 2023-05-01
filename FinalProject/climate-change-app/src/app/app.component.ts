import { Component } from '@angular/core';
import * as d3 from 'd3v4';
import * as jsonFile from '../assets/final_world.geo.json';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'climate-change-app';
  globalData = jsonFile
  titleTag = "";
  yearRange = ["1901", "1902", "1903", "1904", "1905", "1906", "1907", "1908", "1909", "1910", "1911", "1912", "1913", "1914", "1915", "1916", "1917", "1918", "1919", "1920", "1921", "1922", "1923", "1924", "1925", "1926", "1927", "1928", "1929", "1930", "1931", "1932", "1933", "1934", "1935", "1936", "1937", "1938", "1939", "1940", "1941", "1942", "1943", "1944", "1945", "1946", "1947", "1948", "1949", "1950", "1951", "1952", "1953", "1954", "1955", "1956", "1957", "1958", "1959", "1960", "1961", "1962", "1963", "1964", "1965", "1966", "1967", "1968", "1969", "1970", "1971", "1972", "1973", "1974", "1975", "1976", "1977", "1978", "1979", "1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]
  
  ngOnInit() {
    this.createMap(1000, 600, this.globalData)

    let time = 1;
    let interval = setInterval(() => {
       if (time <= 121) {
          this.transitionMap(time)
          time++;
       } else {
          clearInterval(interval);
       }
    }, 1000);
  } 

  createMap(width: number, height: number, dataset: Object) {
    this.titleTag = this.yearRange[0];
    const margin = {top: 10, right: 30, bottom: 10, left: 30};
    width = width - margin.left - margin.right;
    height = height - margin.top - margin.bottom;
    const projection = d3.geoMercator()
                        .scale(130)
                        .center([0,20])
                        .translate([width / 2, height / 2]);
    const path = d3.geoPath().projection(projection);
    const svg = d3.select('.world-map')
                 .append('svg')
                 .attr('viewBox', '0 0 1000 600')

  const colorDomain = [-25, 0, 10, 20, 30, 40]
  const colorLegend = d3.scaleThreshold().range(['#032f60', '#176dae', '#e3a532', '#dd6e6e', '#cc0000']).domain(colorDomain);

  svg.append("g")
  .selectAll("path")
  .data(this.globalData.features)
  .enter()
  .append("path")
  .attr('d', path)
  .style('fill', function(d: any) {
    const value = d['properties']['temp1901'];
    if (value) {
      return colorLegend(d['properties']['temp1901']);
    } else {
      return '#ccc';
  }})
  .style('stroke', '#fff')
  .style('stroke-width', '0.5')
}

transitionMap(i: number) {
  this.titleTag = this.yearRange[i];

  const svg = d3.select('.world-map');
  
  const colorDomain = [-25, 0, 10, 20, 30, 40]
  const colorLegend = d3.scaleThreshold().range(['#032f60', '#176dae', '#e3a532', '#dd6e6e', '#cc0000']).domain(colorDomain);

svg.selectAll('path')
   .data(this.globalData.features)
   .transition()
   .delay(100)
   .duration(1000)
   .style('fill', function(d: any) {
      var year = i + 1900 
      var yearName = "temp" + year
      const value = d['properties'][yearName];
      if (value) {
        return colorLegend(d['properties'][yearName]);
      } else {
        return '#ccc';
      }
   })
}
}
