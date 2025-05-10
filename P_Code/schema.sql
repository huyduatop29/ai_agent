CREATE TABLE metadata(
  id SERIAL PRIMARY KEY,
  element_id TEXT,
  emphasized_text_contents TEXT[],
  emphasized_text_tags TEXT[],
  file_directory TEXT,
  filename TEXT,
  last_modified TEXT,
  page_number INTEGER,
  category TEXT,
  vector_database FLOAT8,
)


