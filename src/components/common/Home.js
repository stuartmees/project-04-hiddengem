import React from 'react'
import SearchBar from './SearchBar'

class Home extends React.Component {
  constructor() {
    super()

    this.state = null
  }

  render() {
    return(
      <div className="container-form">
        <SearchBar />
      </div>
    )
  }
}

export default Home
