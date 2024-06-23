import { useHistory, useParams } from "react-router-dom";
import useFetch from "./useFetch";

const BlogDetails = () => {
  const { id } = useParams();
  const { data: blog, error, isPending } = useFetch('http://127.0.0.1:8000/api/book/'+ id);
  const history = useHistory();

  const handleClick = () => {
    fetch('' + blog.pk, {
      method: 'DELETE'
    }).then(() => {
      history.push('/');
    }) 
  }

  return (
    <div className="blog-details">
      { isPending && <div>Loading...</div> }
      { error && <div>{ error }</div> }
      { blog && (
        <article>
          <h2>{ blog.title }</h2>
          <p>Written by { blog.author.name }</p>
          <div>{ blog.body }</div>

        </article>
      )}
    </div>
  );
}
 
export default BlogDetails;