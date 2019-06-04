import React from 'react'
import axios from 'axios'

class EntriesShow extends React.Component {
  constructor(){
    super()

    this.state = null
  }

  componentDidMount(prevProps){
    axios.get(`/api/entries/${this.props.match.params.id}`)
      .then(res => {
        this.setState(res.data)
        console.log(prevProps)
      })
  }

  render(){
    if(!this.state) return <p>Loading...</p>
    return(
      <div>
        <div className="text-link" onClick={this.props.history.goBack}>&larr; Back to map</div>
        <div className="container-show">
          <section>
            <h1 className="show-title">{this.state.title}</h1>
            <div className="columns">
              <div className="column">
                <h4 className="show-meta">{this.state.location}</h4>
              </div>
              <div className="column">
                <h4 className="show-meta">Uploaded by {this.state.created_by.username}</h4>
              </div>
            </div>
          </section>


        </div>
        <div className="show-image">
          <figure className="image is-16by9">
            <img src={this.state.photo} />
          </figure>
        </div>


        <div className="container-show">
          <p className="show-description">
            {this.state.description.split('\n').map((text, i) =>
              <span key={i}>
                {text}<br />
              </span>
            )}
          </p>
        </div>

      </div>
    )
  }
}

export default EntriesShow
