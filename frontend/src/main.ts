import { bootstrapApplication } from '@angular/platform-browser';
import { provideRouter, withDebuggerTracing } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';
import { AppComponent } from './app/app.component';
import { appRoutes } from './app/app.routes';

bootstrapApplication(AppComponent, {
  providers: [
    provideHttpClient(),
    provideRouter(appRoutes, withDebuggerTracing())
  ]
}).catch(err => console.error(err));
