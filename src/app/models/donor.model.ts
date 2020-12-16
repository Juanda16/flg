export class Donor {
    id?: any;
    documentId?: string;
    documentType?: string;
    legalNature?: boolean;
  }

  export class User {
    id?: any;
    username?: string;
    password?: string;
    first_name?: string;
    last_name? : string;
    email?:string;
    is_active?: boolean;
  }