import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'
import Flash from '../../lib/Flash'

class Register extends React.Component {
  constructor(){
    super()

    this.state = {
      data: {}
    }

    this.handleChange=this.handleChange.bind(this)
    this.handleSubmit=this.handleSubmit.bind(this)
  }

  handleChange(e) {
    const data = { ...this.state.data, [e.target.name]: e.target.value }
    this.setState( {data} )
  }

  handleSubmit(e) {
    e.preventDefault()

    axios.post('/api/register', this.state.data)
      .then(res => {
        Auth.setToken(res.data.token)
        Flash.setMessage('success', res.data.message)
        // this.props.history.push('/login')
      })
      .catch(() => this.setState({ error: 'Invalid credentials' }))
  }

  render(){
    return(
      <form onSubmit={this.handleSubmit}>
        <div>
          <label>Username</label>
          <input
            placeholder="jobloggs"
            name="username"
            onChange={this.handleChange}
          />
        </div>

        <div>
          <label>Email</label>
          <input
            placeholder="josephine@bloggs.com"
            name="email"
            onChange={this.handleChange}
          />
        </div>

        <div>
          <label>Password</label>
          <input
            placeholder="**********"
            name="password"
            onChange={this.handleChange}
          />
        </div>

        <div>
          <label>Password Confirmaiton</label>
          <input
            placeholder="**********"
            name="password_confirmation"
            onChange={this.handleChange}
          />
        </div>

        <button>Login</button>
      </form>
    )
  }
}

export default Register
