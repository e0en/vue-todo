<template>
  <li class="todo-list-item" :class="{ complete: checked }">
    <input type="checkbox" v-model="checked" v-on:change="update" />
    <input type="hidden" :value="itemId" />
    <span class="content" v-on:click="showEdit" v-bind:class="[isEditing ?  'hidden' : '']">{{ content }}</span>
    <input ref="text" type="text" v-model="text" v-bind:class="[isEditing ? '' : 'hidden']"
      v-on:blur="editItem" v-on:keyup.enter="editItem" />
    <button class="delete" v-on:click="deleteItem" v-bind:class="[isEditing ?  '' : 'hidden']">delete</button>
  </li>
</template>

<script>
export default {
  name: 'ListItem',
  props: {
    itemId: String,
    content: String,
    isComplete: Boolean
  },
  data: function () {
    return {
      checked: this.isComplete,
      text: this.content,
      isEditing: false
    }
  },
  methods: {
    update: function () {
      var ev = {
        itemId: this.itemId,
        content: this.content,
        checked: this.checked
      }
      this.$emit('update', ev)
    },
    deleteItem: function () {
      this.$emit('deleteItem', this.itemId)
    },
    showEdit: function () {
      this.isEditing = true
      this.$nextTick(() => {
        console.log(this.$refs.text.focus())
      })
    },
    editItem: function () {
      if (this.isEditing) {
        var ev = {
          itemId: this.itemId,
          content: this.text,
          checked: this.checked
        }
        this.$emit('update', ev)
        this.isEditing = false
      }
    }
  }
}
</script>

<style scoped lang="less">
.complete {
  color: #999;
  text-decoration: line-through;
}
input[type=checkbox] {
  margin-right: 1em;
}
button.delete {
  margin-left: 1em;
}
.hidden {
  display: none;
}
</style>
