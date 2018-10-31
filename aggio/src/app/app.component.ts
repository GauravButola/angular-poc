import { Component } from '@angular/core';
import { Chart } from 'angular-highcharts';
import { map } from 'lodash';

import { AppService } from './app.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  chart: Chart;

  constructor(private appService: AppService) {
    this.loadData();
  }

  loadData() {
    this.appService.getData().subscribe(data => this.renderChart(data));
  }

  renderChart(data) {
    const series = map(data, (quantity, item) => {
      return {name: item, data: [quantity]}
    });
    this.chart = new Chart({
      chart: {
        type: 'column'
      },
      title: {
        text: 'Bakery transactions'
      },
      credits: {
        enabled: false
      },
      xAxis: {
        title: {
          text: 'Item'
        }
      },
      yAxis: {
        title: {
          text: 'Transactions'
        }
      },
      series: series
    });
  }
}
