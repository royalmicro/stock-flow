import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment';
import { AppModule } from '../../app.module';

@Injectable({
  providedIn: AppModule,
})
export class EnvironmentService {
  private env = environment;

  constructor() {}

  get apiUrl(): string {
    return this.env.apiUrl;
  }

  get isProduction(): boolean {
    return this.env.production;
  }

  get featureFlag(): boolean {
    return this.env.featureFlag;
  }

  // Add any other environment-specific getters here
}
