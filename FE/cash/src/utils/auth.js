import auth0 from 'auth0-js'
import EventEmitter from 'eventemitter3'
import router from '@/router'

class AuthService {
  constructor () {
    this.accessToken = ''
    this.idToken = ''
    this.expiresAt = ''
    this.authenticated = this.isAuthenticated()
    this.authNotifier = new EventEmitter()

    this.auth0 = new auth0.WebAuth({
      domain: 'zhk.auth0.com',
      clientID: '9QpScXltE1zfeGsNdNozkI4zYaWoUWDG',
      redirectUri: 'http://localhost:8081/callback',
      responseType: 'token id_token',
      scope: 'openid'
    })
  }

  handleAuthentication () {
    this.auth0.parseHash((err, authResult) => {
      if (authResult && authResult.accessToken && authResult.idToken) {
        this.setSession(authResult)
        router.replace('add')
      } else if (err) {
        router.replace('login')
        // console.log(err)
        alert(`Error: ${err.error}. Check the console for further details.`)
      }
    })
  }

  setSession (authResult) {
    this.accessToken = authResult.accessToken
    this.idToken = authResult.idToken
    this.expiresAt = authResult.expiresIn * 1000 + new Date().getTime()

    this.authNotifier.emit('authChange', { authenticated: true })

    localStorage.setItem('loggedIn', true)
  }

  renewSession () {
    this.auth0.checkSession({}, (err, authResult) => {
      if (authResult && authResult.accessToken && authResult.idToken) {
        this.setSession(authResult)
      } else if (err) {
        this.logout()
        // console.log(err)
        alert(`Could not get a new token (${err.error}: ${err.error_description}).`)
      }
    })
  }

  login () {
    this.auth0.authorize()
  }

  logout () {
    // Clear access token and ID token from local storage
    this.accessToken = null
    this.idToken = null
    this.expiresAt = null
    this.userProfile = null

    this.authNotifier.emit('authChange', false)

    localStorage.removeItem('loggedIn')

    // navigate to the home route
    router.replace('login')
  }

  getAuthenticatedFlag () {
    return localStorage.getItem('loggedIn')
  }

  isAuthenticated () {
    // Check whether the current time is past the
    // access token's expiry time
    return new Date().getTime() < this.expiresAt && this.getAuthenticatedFlag() === 'true'
  }
}

export default new AuthService()
