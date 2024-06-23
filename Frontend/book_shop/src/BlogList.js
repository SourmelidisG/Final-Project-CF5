import { Link } from 'react-router-dom';

const BlogList = ({ blogs }) => {
  return (
    <div className="blog-list">
      {blogs.map(blog => (
        <div className="blog-preview" key={blog.pk} >
          <Link to={`/blogs/${blog.pk}`}>
            <h2>{ blog.title }</h2>
            <p>Written by { blog.author.name }</p>
          </Link>
        </div>
      ))}
    </div>
  );
}
 
export default BlogList;


