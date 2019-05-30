import React from 'react'
import axios from 'axios'
import Select from 'react-select'

const options = [
  { value: 1, label: 'Sleeping' },
  { value: 2, label: 'Eating' },
  { value: 3, label: 'Going' },
  { value: 4, label: 'Doing' }
]

class EntriesNew extends React.Component {
  constructor() {
    super()

    this.state = {
      data: {category_id: null}
    }

    this.handleChange=this.handleChange.bind(this)
    this.handleCategoryChange=this.handleCategoryChange.bind(this)
  }

  handleChange(e) {
    const data = { ...this.state.data, [e.target.name]: e.target.value }
    this.setState( {data} )
  }

  handleCategoryChange(selectedCategory) {
    this.setState({ data: {category_id: selectedCategory.value} })
    console.log('Category selected:', selectedCategory)
  }

  handleSubmit(e) {
    e.preventDefault()

    axios.post('/api/entries/new', this.state.data)
      .then(this.props.history.push('/entries'))
      .catch(() => this.setState({ error: 'Invalid credentials' }))
  }

  componentDidMount() {
  }

  render() {
    const { selectedCategory } = this.state

    return(
      <form onSubmit={this.handleSubmit}>
        <div>
          <label>Category</label>
          <Select
            options={options}
            value={selectedCategory}
            name='category_id'
            onChange={this.handleCategoryChange}
          />
        </div>

        <div>
          <label>Title</label>
          <input
            placeholder="Main tag line!"
            name="title"
            onChange={this.handleChange}
          />
        </div>

        <div>
          <label>Description</label>
          <input
            placeholder="josephine@bloggs.com"
            name="email"
            onChange={this.handleChange}
          />
        </div>

        <div>
          <label>Category</label>
          <input
            placeholder="josephine@bloggs.com"
            name="Pick from the following"
            onChange={this.handleChange}
          />
        </div>

        <div>
          <label>Website</label>
          <input
            placeholder="www.greatplace.com"
            name="website"
            onChange={this.handleChange}
          />
        </div>

        <div>
          <label>Nearest Town</label>
          <input
            placeholder="Puskkar"
            name="email"
            onChange={this.handleChange}
          />
        </div>
      </form>
    )
  }
}

export default EntriesNew


// title = Required(str)
// description = Required(str)
// category = Required('Category')
// website = Optional(str)
// photo = Optional(str)
// town = Required(str)
// state = Required('State')
// created_by = Optional('User')
// lng = Required(float)
// lat = Required(float)
