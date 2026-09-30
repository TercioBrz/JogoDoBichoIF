export interface Response {
  success: string;
  data: Record<string, string>;
  errors: Record<string, Record<string, string>>;
  message: string;
}