import React from 'react'
import { withRouter } from 'react-router-dom'

class SearchBar extends React.Component {
  constructor(){
    super()

    this.state={
      searchTerm: []
    }

    this.handleChange=this.handleChange.bind(this)
    this.handleSubmit=this.handleSubmit.bind(this)
  }

  handleChange(e){
    this.setState( { searchTerm: e.target.value } )
    console.log(this.state)
  }

  handleSubmit(e){
    e.preventDefault()
    this.props.history.push('/entries?search=' + this.state.searchTerm)
  }

  render(){
    return(
      <form onSubmit={this.handleSubmit} className="search-bar">
        <input
          className="input"
          placeholder="What you looking for?"
          onChange={this.handleChange}
        />
        <button >Find it</button>
      </form>
    )
  }
}

export default withRouter(SearchBar)
