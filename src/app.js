import React from 'react'
import ReactDOM from 'react-dom'
import { HashRouter as Router, Switch, Route } from 'react-router-dom'
import EntriesIndex from './components/entries/Index.js'


class App extends React.Component {

  render(){
    return(
      <Router>
        <main>
          <Switch>
            <Route path="/entries" component={EntriesIndex}/>
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
