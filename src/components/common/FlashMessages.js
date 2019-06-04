import React from 'react'
import Flash from '../../lib/Flash'
import { withRouter } from 'react-router-dom'

class FlashMessages extends React.Component {
  constructor() {
    super()

    this.state = { messages: null }
  }

  componentDidUpdate() {
    const messages = Flash.getMessages()
    if(!messages) return false
    this.setState({ messages })
    Flash.clearMessages()
    setTimeout(() => this.setState({ messages: null }), 3500)
  }

  render() {
    return (
      this.state.messages && Object.keys(this.state.messages).map(type =>
        <div key={type} className={'flash-message'}>
          <p>
            {this.state.messages[type]}
          </p>
        </div>
      )
    )
  }
}

export default withRouter(FlashMessages)
