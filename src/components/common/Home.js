import React from 'react'
import SearchBar from './SearchBar'

class Home extends React.Component {
  constructor() {
    super()

    this.state = null
  }

  render() {
    return(
      <div>
        <section className="container-form">
          <SearchBar />
        </section>
        <section className="columns home-images">
          <div className="column home-image-1">

          </div>
          <div className="column home-image-2">

          </div>
          <div className="column home-image-3">

          </div>
        </section>
      </div>

    )
  }
}

export default Home
