import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const state = {
  users: [],
  products: []
}

const mutations = {
  SET_USERS(state, users) {
    state.users = users
  },
  SET_PRODUCTS(state, products) {
    state.products = products
  }
}

const actions = {
  getUsers({ commit }) {
    axios.get('/api/users/')
      .then(response => {
        commit('SET_USERS', response.data)
      })
      .catch(error => {
        console.log(error)
      })
  },
  getProducts({ commit }) {
    axios.get('/api/products/')
      .then(response => {
        commit('SET_PRODUCTS', response.data)
      })
      .catch(error => {
        console.log(error)
      })
  }
}

const getters = {
  getUserById: (state) => (id) => {
    return state.users.find(user => user.id === id)
  },
  getProductById: (state) => (id) => {
    return state.products.find(product => product.id === id)
  }
}

const userModule = {
  state: {
    users: []
  },
  mutations: {
    SET_USERS(state, users) {
      state.users = users
    }
  },
  actions: {
    getUsers({ commit }) {
      axios.get('/api/users/')
        .then(response => {
          commit('SET_USERS', response.data)
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  getters: {
    getUserById: (state) => (id) => {
      return state.users.find(user => user.id === id)
    }
  }
}

const productModule = {
  state: {
    products: []
  },
  mutations: {
    SET_PRODUCTS(state, products) {
      state.products = products
    }
  },
  actions: {
    getProducts({ commit }) {
      axios.get('/api/products/')
        .then(response => {
          commit('SET_PRODUCTS', response.data)
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  getters: {
    getProductById: (state) => (id) => {
      return state.products.find(product => product.id === id)
    }
  }
}

export default new Vuex.Store({
  state,
  mutations,
  actions,
  getters,
  modules: {
    user: userModule,
    product: productModule
  }
})
