import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { initializeApp } from 'firebase/app';
import { getAuth, signInWithEmailAndPassword, GoogleAuthProvider, signInWithPopup, signOut } from 'firebase/auth';
import { firebaseConfig } from '../core/firebase.config';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private auth = getAuth(initializeApp(firebaseConfig));
  private apiBase = 'http://localhost:8000/api/auth';

  constructor(private http: HttpClient) {}

  async loginWithEmail(email: string, password: string) {
    const credential = await signInWithEmailAndPassword(this.auth, email, password);
    return credential.user.getIdToken();
  }

  async loginWithGoogle() {
    const provider = new GoogleAuthProvider();
    const credential = await signInWithPopup(this.auth, provider);
    return credential.user.getIdToken();
  }

  async logout() {
    await signOut(this.auth);
  }

  verifyToken(idToken: string) {
    return this.http.post(`${this.apiBase}/verify`, { token: idToken });
  }
}
