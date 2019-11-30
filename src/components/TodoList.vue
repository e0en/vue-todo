<template>
<div class="container todo-list">
  <form class="field" v-on:submit.prevent="addNewItem">
    <p class="control">
      <label for="newContent">Add a new task</label><br />
      <input class="input" type="text" name="newContent" v-model="newContent" />
    </p>
  </form>
  <div class="field">
    <button class="button is-small" v-on:click="toggleHideCompleted">{{ hideCompleted ? "Show" : "Hide" }} completed</button>
  </div>
  <ul>
    <TodoItem v-for="i in items" :key="i.itemId"
      :itemId="i.itemId" :content="i.content" :isComplete="i.isComplete"
      v-on:update="update" v-on:deleteItem="deleteItem"
      v-show="(!i.isComplete) | (!hideCompleted)"
    />
  </ul>
  <div class="container" v-show="isLoggedIn">
    <button class="button is-danger is-light" v-on:click="logout">Logout</button>
  </div>
  <Login ref="login" :isActive="!isLoggedIn" v-on:login="handleLogin" />
</div>
</template>

<script>
// @ is an alias to /src
import backendUrl from '@/settings.js'
import axios from 'axios'

axios.defaults.withCredentials = true

export default {
  name: 'TodoList',
  data: function () {
    return {
      newContent: '',
      items: [],
      hideCompleted: false,
      isLoggedIn: true
    }
  },
  components: {
    TodoItem: () => import('@/components/TodoItem.vue'),
    Login: () => import('@/components/Login.vue')
  },
  methods: {
    getAll: function () {
      const comp = this
      axios.get(backendUrl + '/todo')
        .then((res) => {
          comp.isLoggedIn = true
          comp.items = []
          res.data.forEach(d => comp.items.push(d))
        })
        .catch(() => {
          comp.isLoggedIn = false
        })
    },
    update: function (ev) {
      this.items.forEach(function (item) {
        if (item.itemId === ev.itemId) {
          item.isComplete = ev.checked
          item.content = ev.content
          axios.put(backendUrl + '/todo/' + item.itemId, item)
            .then(() => {
            })
        }
      })
    },
    addNewItem: function (ev) {
      var newId = this.items.length.toString()
      var newItem = { itemId: newId, content: this.newContent, isComplete: false }
      this.items.push(newItem)
      axios.post(backendUrl + '/todo', newItem)
        .then(() => {
        })

      this.newContent = ''
      return false
    },
    deleteItem: function (itemId) {
      axios.delete(backendUrl + '/todo/' + itemId)
        .then(() => {
          this.items = this.items.filter(function (item) {
            return item.itemId !== itemId
          })
        })
    },
    toggleHideCompleted: function () {
      this.hideCompleted = !this.hideCompleted
    },
    handleLogin: function (isSuccess) {
      if (isSuccess) {
        this.isLoggedIn = true
        this.$refs.login.isActive = false
        this.getAll()
      } else {
        this.isLoggedIn = false
        this.$refs.login.isActive = true
      }
    },
    logout: function () {
      axios.get(backendUrl + '/logout')
        .then(() => {
          this.items = []
          this.isLoggedIn = false
          this.$refs.login.isActive = true
        })
    }
  },
  mounted: function () {
    this.getAll()
  }
}
</script>

<style lang="scss" scoped>
div.todo-list {
  margin: 1em auto;
  text-align: left;
}
.content ul {
  list-style-type: none;
  margin-left: 0;
  padding-left: 0;
}
.hidden {
  display: none;
}
</style>
