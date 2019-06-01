import React from 'react'
import ReactDOM from 'react-dom'
import './styles.scss'
import { HashRouter as Router, Switch, Route } from 'react-router-dom'
import EntriesIndex from './components/entries/Index.js'
import EntriesShow from './components/entries/Show.js'

import Login from './components/auth/Login.js'
import Register from './components/auth/Register.js'
import FlashMessages from './components/common/FlashMessages.js'
import EntriesNew from './components/entries/New.js'
import Navbar from './components/common/Navbar.js'
import Home from './components/common/Home.js'

import 'bulma'

class App extends React.Component {
  render(){
    return(
      <Router>
        <main>
          <FlashMessages />
          <Navbar />
          <Switch>
            <Route path="/entries/new" component={EntriesNew} />
            <Route path="/entries/:id" component={EntriesShow} />
            <Route path="/entries" component={EntriesIndex} />
            <Route path="/login" component={Login} />
            <Route path="/register" component={Register} />
            <Route path="/" component={Home} />
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
