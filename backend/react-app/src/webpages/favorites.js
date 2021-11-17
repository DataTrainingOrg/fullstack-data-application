//file: src/webpages/favorites.js
import React, { useEffect } from 'react';
const Favorites = () => {
    useEffect(() => {
        document.title = 'My Favorites';
    });
    return (
        <div>
            <h1>Book App</h1>
            <p>These are my favorite books</p>
        </div>
    );
};
export default Favorites;