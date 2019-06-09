import React from 'react'
import { withRouter } from 'react-router-dom'
import qs from 'query-string'

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
  }

  //Obtains current search prop and constructs the URL appropriately before re-direct.
  handleSubmit(e){
    e.preventDefault()

    const searchProp = qs.parse(this.props.location.search)

    if (!Object.keys(searchProp).includes('filtercategory')){
      this.props.history.push('/entries?search='+this.state.searchTerm)
    } else {
      this.props.history.push('/entries?filtercategory='+searchProp.filtercategory+'&search='+this.state.searchTerm)
    }
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
