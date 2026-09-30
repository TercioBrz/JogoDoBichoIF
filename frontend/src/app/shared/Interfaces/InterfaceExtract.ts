export interface Bet {
  id: number;
  win: number;
  loss: number;
  bet: number;
  created_at: string;
}

export interface BetResponse {
  data: Bet[];
}