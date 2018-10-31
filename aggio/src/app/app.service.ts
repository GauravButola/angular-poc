import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { map } from 'rxjs/operators';

@Injectable()
export class AppService {
  constructor (
    private http: Http
  ) {}

  getData() {
    // TODO: Pick API URL from config
    return this.http.get(`http://localhost:5000/transactions`)
    .pipe(map((res:Response) => res.json()));
  }

}
