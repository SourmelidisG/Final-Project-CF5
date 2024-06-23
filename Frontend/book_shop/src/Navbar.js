import { Link } from "react-router-dom";

const Navbar = () => {
  const page_tile = "Book Library";
  return (
    <nav className="navbar">
      <h1>{page_tile}</h1>
      <div className="links">
        <Link to="/">Home</Link>
         <Link to="/authors" style={{ 
          color: 'white', 
          backgroundColor: '#f1356d',
          borderRadius: '8px' 
        }}>Athors</Link>
        <a 
          href="http://127.0.0.1:8000/admin/login/?next=/admin/" 
          target="_blank" 
          rel="noopener noreferrer"
          style={{ 
            color: 'white', 
            backgroundColor: '#f1356d',
            borderRadius: '8px' 
          }}
        >
          Admin
        </a>
      </div>
    </nav>
  );
}
 
export default Navbar;