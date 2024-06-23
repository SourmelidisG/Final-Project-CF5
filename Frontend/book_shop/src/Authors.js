
import useFetch from "./useFetch";
import AuthorList from "./AuthorList";
const Author = () => {
  const { error, isPending, data: authors } = useFetch('http://127.0.0.1:8000/api/author')
  console.log(authors);
  return (
    <div className="home">
      { error && <div>{ error }</div> }
      { isPending && <div>Loading...</div> }
      { authors && <AuthorList authors={authors} /> }
    </div>
  );
}
 
export default Author;
