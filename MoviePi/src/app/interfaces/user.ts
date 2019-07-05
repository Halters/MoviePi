import { Genre } from './genre';

export interface User {
  uuid: string;
  username: string;
  password: string;
  age: number;
  genres: Array<Genre>;
}
