import React from 'react';
import { Link } from 'react-router-dom';

const AuthorList = ({ authors }) => {
  return (
    <div className="author-list">
      {authors.map(author => (
        <div className="author-preview" key={author.pk}>
          <Link to={`/authors/${author.pk}`}>
            {author.image && <img className="author-image" src={author.image} alt={`${author.name}'s profile`} />}
            <h2>{author.name}</h2>
          </Link>
        </div>
      ))}
    </div>
  );
}

export default AuthorList;
