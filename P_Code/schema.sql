-- Tài liệu trước khi nhúng
create table documents(
    id SERIAL PRIMARY KEY,
    filename TEXT,
    file_directory TEXT,
    source TEXT,
    last_modified TIMESTAMP,
    filetype TEXT,
    languages TEXT[]
);

-- Các chunk tài liệu được chia nhỏ
create table chunks(
    id SERIAL PRIMARY KEY,
    document_id INTEGER NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    page_number INTEGER,
    element_id TEXT,
    page_content TEXT
);

-- Các từ được nhấn mạnh có thể là nội dung chính của văn bản
CREATE TABLE emphasized_text(
    id SERIAL PRIMARY KEY,
    chunk_id INTEGER NOT NULL REFERENCES chunks(id) ON DELETE CASCADE,
    content TEXT,
    tag text
);
-- các vector thu được sau khi nhúng các chunk
create table embeddings(
    id SERIAL PRIMARY KEY,
    chunk_id INTEGER NOT NULL REFERENCES chunks(id) ON DELETE CASCADE,
    vector_data vector(1024)
);


