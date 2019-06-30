import { ApiResonseStatus } from './../enums/api-resonse-status.enum';

export interface ApiResponse {
  responseStatus: ApiResonseStatus;
  message: string;
  data: object;
}
