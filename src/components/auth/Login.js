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
    if(!e.target.value) delete data[e.target.name]
    this.setState( {data} )
  }

  handleSubmit(e) {
    e.preventDefault()

    axios.post('/api/login', this.state.data)
      .then(res => {
        Auth.setToken(res.data.token)

        Flash.setMessage('success', res.data.message)
        
        this.props.history.push('/')
      })
      .catch(error => {
        this.setState(error.response.data)
      })
  }

  render(){
    return(
      <form onSubmit={this.handleSubmit} className="form container-form">
        <h1 className="logo">Login</h1>
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
          <button>Login</button>
        </div>

        {this.state.error &&
          <div className="error-message">{this.state.error}</div>}
      </form>
    )
  }
}

export default Login
