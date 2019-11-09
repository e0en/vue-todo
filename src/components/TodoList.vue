<template>
<div class="todo-list content">
  <h1>{{ name }}</h1>
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
</div>
</template>

<script>
// @ is an alias to /src
import TodoItem from '@/components/TodoItem.vue'
import backendUrl from '@/settings.js'
import axios from 'axios'

export default {
  name: 'TodoList',
  props: {
    name: String
  },
  data: function () {
    return {
      newContent: '',
      items: [],
      hideCompleted: false
    }
  },
  components: {
    TodoItem
  },
  methods: {
    getAll: function () {
      var comp = this
      axios.get(backendUrl + '/todo')
        .then((res) => {
          res.data.forEach(d => comp.items.push(d))
          console.log(res.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    update: function (ev) {
      console.log(ev)
      this.items.forEach(function (item) {
        if (item.itemId === ev.itemId) {
          item.isComplete = ev.checked
          item.content = ev.content
          axios.put(backendUrl + '/todo/' + item.itemId, item)
            .then(() => {
              console.log('update complete')
            })
            .catch((error) => {
              console.log(error)
            })
        }
      })
    },
    addNewItem: function (ev) {
      console.log(this.newContent)
      var newId = this.items.length.toString()
      var newItem = { itemId: newId, content: this.newContent, isComplete: false }
      this.items.push(newItem)
      axios.post(backendUrl + '/todo', newItem)
        .then(() => {
          console.log('post complete')
        })
        .catch((error) => {
          console.log(error)
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
          console.log('deleted ' + itemId)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    toggleHideCompleted: function () {
      this.hideCompleted = !this.hideCompleted
      this.items.forEach(item => {
        if (item.isComplete) {
          console.log(item)
        }
      })
    }
  },
  created: function () {
    this.getAll()
  }
}
</script>

<style lang="scss" scoped>
div.todo-list {
  margin: 0 auto;
  max-width: 900px;
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
