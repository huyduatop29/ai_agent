-- tìm tăt cả các file được upload
select * from documents;

-- tìm thông tin tài liệu qua id hoặc filename
select * from documents where filename ='kiemtra.docx';
select * from documents where id = 3;

-- kiểm tra xem tài liệu đã tồn tại chưa dựa trên source hoặc filename
select exists (select 1 from documents where filename = 'kiemtra.docx') as file_exists;
select exists (select 1 from documents where source = 'kiemtra.docx') as file_exists;


--Lấy tất cả các chunks thuộc một documents
select * from chunks as c 
join documents as d on d.id = c.document_id
where d.filename = 'Chi_Huuyenshare.xlsx'
order by c.id asc;

-- Truy xuất page_content theo chunk_id hoặc theo document_id
select page_content from chunks where document_id = 22;
select page_content from chunks where id = 22;

-- Tìm chunks theo một số tiêu chí như: page_number, element_id
select * from chunks as c
join documents as d on c.document_id = d.id
where d.filename = 'Chi_Huuyenshare.xlsx' and c.page_number = 3 
order by c.document_id asc;

--Truy xuất vector embedding theo chunk_id
select c.id , c.page_content, e.vector_data 
from embeddings as e 
join chunks as c on c.id = e.chunk_id 
where e.chunk_id= 200 
order by c.id asc; 

--Trích tất cả embedding để thực hiện tính toán khoảng cách (cosine similarity, ANN...)
select id, embeddings.vector_data from embeddings order by id asc;
--Tìm top k chunks gàn nhất với một ebeđing đầu vào z



--Tìm các emphasized_text theo tag hoặc content.
select * from emphasized_text 
where content = 'TRƯỜNG ĐẠI HỌC GIAO THÔNG VẬN TẢI';

--Tìm documents theo ngôn ngữ hoặc loại file.
select * from documents where languages @> ARRAY['eng'];
