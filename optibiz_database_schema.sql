CREATE TABLE Users (
  user_id INT PRIMARY KEY,
  username VARCHAR(50),
  password VARCHAR(255),
  email VARCHAR(100),
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  role VARCHAR(20)
);

CREATE TABLE Organizations (
  organization_id INT PRIMARY KEY,
  organization_name VARCHAR(100),
  address VARCHAR(200),
  phone VARCHAR(20)
);

CREATE TABLE Projects (
  project_id INT PRIMARY KEY,
  project_name VARCHAR(100),
  organization_id INT,
  start_date DATE,
  end_date DATE,
  status VARCHAR(20),
  FOREIGN KEY (organization_id) REFERENCES Organizations(organization_id)
);

CREATE TABLE Inventory (
  inventory_id INT PRIMARY KEY,
  item_name VARCHAR(100),
  item_description VARCHAR(200),
  quantity INT,
  organization_id INT,
  FOREIGN KEY (organization_id) REFERENCES Organizations(organization_id)
);

CREATE TABLE Tasks (
  task_id INT PRIMARY KEY,
  task_name VARCHAR(100),
  project_id INT,
  user_id INT,
  start_date DATE,
  end_date DATE,
  status VARCHAR(20),
  FOREIGN KEY (project_id) REFERENCES Projects(project_id),
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Reports (
  report_id INT PRIMARY KEY,
  report_name VARCHAR(100),
  organization_id INT,
  user_id INT,
  creation_date DATE,
  report_data TEXT,
  FOREIGN KEY (organization_id) REFERENCES Organizations(organization_id),
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
);