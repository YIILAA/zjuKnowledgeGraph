<template>
  <div class="app-container">
    <header>
      <MyHeader></MyHeader>
    </header>

    <div class="body container-fluid">
      <div class="row">
        <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
          <div class="position-sticky pt-3 sidebar-sticky">
            <ul class="nav flex-column">
              <li class="nav-item">
                <RouterLink
                  to="/"
                  class="nav-link"
                  :class="activeItem === 0 ? 'active' : ''"
                  @click="activeItem = 0"
                  >项目简介</RouterLink
                >
              </li>
              <li class="nav-item">
                <RouterLink
                  to="/query"
                  class="nav-link"
                  :class="activeItem === 1 ? 'active' : ''"
                  @click="activeItem = 1"
                  >图谱问答</RouterLink
                >
              </li>
            </ul>
          </div>
        </nav>
        <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
          <RouterView />
        </main>
      </div>
    </div>
  </div>
</template>

<script>
// import { RouterLink, RouterView } from 'vue-router'
import MyHeader from '@/components/MyHeader.vue'

export default {
  data() {
    return {
      activeItem: 0
    }
  },
  components: {
    MyHeader
  }
}
</script>

<style lang="less" scoped>
.body {
  padding: 56px 0 0;
  /* Height of navbar */
}

/*
 * Sidebar
 */

.sidebar {
  position: fixed;
  top: 0;
  /* rtl:raw:
  right: 0;
  */
  bottom: 0;
  /* rtl:remove */
  left: 0;
  z-index: 100;
  /* Behind the navbar */
  padding: 48px 0 0;
  /* Height of navbar */
  box-shadow: inset -1px 0 0 rgba(0, 0, 0, 0.1);
}

.sidebar-sticky {
  height: calc(100vh - 48px);
  overflow-x: hidden;
  overflow-y: auto;
  /* Scrollable contents if viewport is shorter than content. */
}

.sidebar .nav-link {
  font-weight: 500;
  color: #333;
}

.sidebar .nav-link {
  font-weight: 500;
  color: #333;
}

.sidebar .nav-link .feather {
  margin-right: 4px;
  color: #727272;
}

.sidebar .nav-link.active {
  color: #2470dc;
}

.sidebar .nav-link:hover .feather,
.sidebar .nav-link.active .feather {
  color: inherit;
}

.sidebar-heading {
  font-size: 0.75rem;
}
</style>
