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
      <form onSubmit={this.handleSubmit} className="form container-form">
        <h1 className="logo">Register</h1>
        <div className="field">
          <label className="label">Username</label>
          <div className="control">
            <input
              className="input"
              placeholder="jobloggs"
              name="username"
              onChange={this.handleChange}
            />
          </div>
        </div>
        <div className="control">
        </div>

        <div className="field">
          <label className="label">Email</label>
          <div className="control">
            <input
              className="input"
              placeholder="josephine@bloggs.com"
              name="email"
              onChange={this.handleChange}
            />
          </div>
        </div>

        <div className="field">
          <label className="label">Password</label>
          <div className="control">
            <input
              className="input"
              placeholder="**********"
              name="password"
              onChange={this.handleChange}
            />
          </div>
        </div>

        <div className="field">
          <label className="label">Password Confirmaiton</label>
          <div className="control">
            <input
              className="input"
              placeholder="**********"
              name="password_confirmation"
              onChange={this.handleChange}
            />
          </div>
        </div>

        <div className="form-submit">
          <button>Register</button>
        </div>
      </form>
    )
  }
}

export default Register
