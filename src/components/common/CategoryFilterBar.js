import React from 'react'
import { withRouter } from 'react-router-dom'
import Select from 'react-select'
import qs from 'query-string'

const categoryOptions = [
  { value: 1, label: 'Sleeping' },
  { value: 2, label: 'Eating' },
  { value: 3, label: 'Going' },
  { value: 4, label: 'Doing' }
]

const selectStyles = {
  control: (provided, state) => ({
    ...provided,
    border: '0px',
    boxShadow: '0px 2px 12px -4px rgba(145,140,145,0.67)',
    fontFamily: 'Montserrat'
  }),
  option: (provided, state) => ({
    ...provided,
    fontFamily: 'Montserrat'
  })
}

class CategoryFilterBar extends React.Component {
  constructor(){
    super()

    this.state={
      data: {}
    }

    this.handleCategoryChange=this.handleCategoryChange.bind(this)
    this.handleSubmit=this.handleSubmit.bind(this)
  }

  handleCategoryChange(selectedCategory) {
    const data = {  filterCategoryTerm: selectedCategory.label}
    this.setState( {data} )
  }

  handleSubmit(e){
    e.preventDefault()

    const searchProp = qs.parse(this.props.location.search)

    if (Object.keys(searchProp).length === 0 || !Object.keys(searchProp).includes('search')){
      this.props.history.push('/entries?'+'filtercategory=' + this.state.data.filterCategoryTerm)

    } else if (Object.keys(searchProp).includes('search') && !Object.keys(searchProp).includes('filtercategory')){
      this.props.history.push('/entries?'+'search='+searchProp.search+'&filtercategory='+this.state.data.filterCategoryTerm)

    } else {
      this.props.history.push('/entries?search='+searchProp.search+'&filtercategory='+this.state.data.filterCategoryTerm)
    }
  }


  render(){
    const { category } = this.state.data

    return(
      <form onSubmit={this.handleSubmit} className="filter-bar">
        <Select
          styles={selectStyles}
          options={categoryOptions}
          value={category}
          name='category_id'
          onChange={this.handleCategoryChange}
          placeholder='Select a category'
        />
        <button >Filter it</button>
      </form>
    )
  }
}

export default withRouter(CategoryFilterBar)
