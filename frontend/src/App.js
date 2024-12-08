import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import SearchResults from './components/SearchResults';

const App = () => {
  return (
    <Router>
      <div>
        <Switch>
          <Route exact path="/" component={SearchResults} />
          {/* Add more routes here for different pages */}
        </Switch>
      </div>
    </Router>
  );
};

export default App;
