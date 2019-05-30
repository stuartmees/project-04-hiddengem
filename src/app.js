import React from 'react'
import ReactDOM from 'react-dom'
import { HashRouter as Router, Switch, Route } from 'react-router-dom'
import EntriesIndex from './components/entries/Index.js'
import Login from './components/auth/Login.js'
import Register from './components/auth/Register.js'
import FlashMessages from './components/common/FlashMessages.js'
import EntriesNew from './components/entries/New.js'

class App extends React.Component {
  render(){
    return(
      <Router>
        <main>
          <FlashMessages />
          <Switch>
            <Route path="/entries/new" component={EntriesNew} />
            <Route path="/entries" component={EntriesIndex} />
            <Route path="/login" component={Login} />
            <Route path="/register" component={Register} />
          </Switch>
        </main>
      </Router>
    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
