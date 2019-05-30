import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth.js'
import Flash from '../../lib/Flash.js'

class Login extends React.Component {
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

    axios.post('/api/login', this.state.data)
      .then(res => {
        Auth.setToken(res.data.token)
        Flash.setMessage('success', res.data.message)
        this.props.history.push('/entries')
      })
      .catch(() => this.setState({ error: 'Invalid credentials' }))
  }

  render(){
    return(
      <form onSubmit={this.handleSubmit}>
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

export default Login
