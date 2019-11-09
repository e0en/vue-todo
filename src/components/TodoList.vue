<template>
<div class="todo-list">
  <h1>{{ name }}</h1>
  <form v-on:submit.prevent="addNewItem">
    <label for="newContent">Add new task</label><br />
    <input type="text" name="newContent" v-model="newContent" />
  </form>
  <ul>
    <ListItem v-for="i in items" :key="i.itemId"
      :itemId="i.itemId" :content="i.content" :isComplete="i.isComplete"
      v-on:update="update" v-on:deleteItem="deleteItem"
    />
  </ul>
</div>
</template>

<script>
// @ is an alias to /src
import ListItem from '@/components/ListItem.vue'
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
      items: []
    }
  },
  components: {
    ListItem
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
    }
  },
  created: function () {
    this.getAll()
  }
}
</script>

<style scoped lang="less">
div.todo-list {
  margin: 0 auto;
  max-width: 900px;
  text-align: left;
}
ul {
  list-style-type: none;
  line-height: 2em;
  margin-left: 0;
  padding-left: 0;
}
</style>
