import React from 'react'
import axios from 'axios'

class EntriesShow extends React.Component {
  constructor(){
    super()

    this.state = null
  }

  componentDidMount(){
    axios.get(`/api/entries/${this.props.match.params.id}`)
      .then(res => this.setState(res.data))
  }



  render(){
    if(!this.state) return <p>Loading...</p>
    return(
      <div>
        <div className="container-show">
          <h1 className="title is-1">{this.state.title}</h1>
          <div className="columns">
            <div className="column">
              <h4 className="subtitle is-4">{this.state.location}</h4>
            </div>
            <div className="column">
              <h4 className="subtitle is-4">Uploaded by {this.state.created_by.username}</h4>
            </div>
          </div>
        </div>
        <div>
          <figure className="image is-16by9">
            <img src={this.state.photo} />
          </figure>
        </div>
        <div className="container-show">
          <div>{this.state.description}</div>
        </div>
      </div>
    )
  }
}

export default EntriesShow
