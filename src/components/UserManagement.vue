<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="users"
          :search="search"
          :sort-by.sync="sortBy"
          :sort-desc.sync="sortDesc"
          :page.sync="page"
          :items-per-page.sync="itemsPerPage"
          :server-items-length="totalUsers"
          @update:search="fetchUsers"
          @update:pagination="fetchUsers"
        >
          <template v-slot:top>
            <v-toolbar flat>
              <v-toolbar-title>User Management</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-text-field
                v-model="search"
                append-icon="mdi-magnify"
                label="Search"
                single-line
                hide-details
              ></v-text-field>
              <v-spacer></v-spacer>
              <v-dialog v-model="userDialog" max-width="600px">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                    icon
                    color="primary"
                    class="ma-2"
                    v-bind="attrs"
                    v-on="on"
                  >
                    <v-icon>mdi-plus</v-icon>
                  </v-btn>
                </template>
                <user-form
                  :user="selectedUser"
                  @submit="handleUserSubmit"
                  @close="closeUserDialog"
                ></user-form>
              </v-dialog>
            </v-toolbar>
          </template>
          <template v-slot:item.actions="{ item }">
            <v-icon small class="mr-2" @click="editUser(item)">
              mdi-pencil
            </v-icon>
            <v-icon small @click="deleteUser(item.id)">mdi-delete</v-icon>
          </template>
        </v-data-table>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import axios from "axios";
import UserForm from "./UserForm.vue";

export default {
  name: "UserManagement",
  components: {
    UserForm,
  },
  data() {
    return {
      headers: [
        { text: "ID", value: "id" },
        { text: "Name", value: "name" },
        { text: "Email", value: "email" },
        { text: "Actions", value: "actions", sortable: false },
      ],
      users: [],
      search: "",
      sortBy: "id",
      sortDesc: false,
      page: 1,
      itemsPerPage: 10,
      totalUsers: 0,
      userDialog: false,
      selectedUser: null,
    };
  },
  methods: {
    async fetchUsers() {
      // Implement Axios request to fetch users from the backend API
      // Update users, totalUsers based on the API response
    },
    addUser() {
      this.selectedUser = null
      this.userDialog = true;
    },
    editUser(user) {
      this.selectedUser = { ...user };
      this.userDialog = true;
    },
    async deleteUser(userId) {
      // Implement Axios request to delete the user from the backend API
      // Update the user list after successful deletion
    },
    async handleUserSubmit(user) {
      if (user.id) {
        // Implement Axios request to update the user in the backend API
      } else {
        // Implement Axios request to create the user in the backend API
      }
      // Update the user list after successful creation or update
      this.closeUserDialog();
    },
    closeUserDialog() {
      this.userDialog = false;
      this.selectedUser = null;
    },
  },
  mounted() {
    this.fetchUsers();
  },
};
</script>
