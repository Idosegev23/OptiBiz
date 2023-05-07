CREATE TABLE users (
  user_id SERIAL PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  role_id INTEGER
);

CREATE TABLE organizations (
  org_id SERIAL PRIMARY KEY,
  org_name VARCHAR(100) NOT NULL,
  org_description TEXT,
  org_address VARCHAR(255),
  org_phone_number VARCHAR(20),
  org_email VARCHAR(100),
  org_website VARCHAR(100)
);

CREATE TABLE projects (
  project_id SERIAL PRIMARY KEY,
  project_name VARCHAR(100) NOT NULL,
  project_description TEXT,
  start_date DATE,
  end_date DATE,
  org_id INTEGER REFERENCES organizations(org_id)
);

CREATE TABLE inventory (
  item_id SERIAL PRIMARY KEY,
  item_name VARCHAR(100) NOT NULL,
  item_description TEXT,
  item_quantity INTEGER NOT NULL,
  item_price DECIMAL(10, 2) NOT NULL,
  item_category VARCHAR(50)
);

CREATE TABLE tasks (
  task_id SERIAL PRIMARY KEY,
  task_name VARCHAR(100) NOT NULL,
  task_description TEXT,
  start_date DATE,
  end_date DATE,
  project_id INTEGER REFERENCES projects(project_id),
  assigned_to INTEGER REFERENCES users(user_id)
);

CREATE TABLE reports (
  report_id SERIAL PRIMARY KEY,
  report_name VARCHAR(100) NOT NULL,
  report_description TEXT,
  report_date DATE,
  project_id INTEGER REFERENCES projects(project_id),
  user_id INTEGER REFERENCES users(user_id)
);