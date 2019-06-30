import { User } from './user';

export interface AuthResponse {
  userInfos: User;
  JWT: string;
  exp: number;
}
