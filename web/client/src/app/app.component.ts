import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
  <router-outlet />
  `,
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'stock-flow';
}
