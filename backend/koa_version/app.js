const Koa = require('koa');
const app = new Koa();

const admin = {
  username: 'admin',
  password: 'password'
}

const userList = []

const sessions = [
  // {
  //   username: 'user1',
  //   token: 'asd8ufj234ro87ujw',
  //   grade: 'user'
  // }
]

function token_gen() {
  return Math.random().toString()
}

// body parse
async function body_parse(ctx, next) {
  if (ctx.request.get('Content-Type') === 'application/json') {
    ctx.body = JSON.parse((await ctx.req.toArray()).toString())
  }
  next()
}

app.use(body_parse)

// userGradeentity parse
app.use(async (ctx, next) => {
  if (!ctx.body.token) {
    next()
    return
  }

  let token = ctx.body.token
  for (let session of sessions) {
    if (session.token === token) {
      ctx.userGrade = session.grade
      break
    }
  }

  next()
})

// register
app.use(async (ctx, next) => {
  if (ctx.req.url === '/register') {
    userList.push({
      username: ctx.body.username,
      password: ctx.body.password
    })
    console.log(userList)
  } else {
    next()
  }
})

// login
app.use(async (ctx, next) => {
  if (ctx.req.url === '/login') {
    let session = {}
    if (ctx.body.username && ctx.body.password) {
      if (ctx.body.username === admin.username && ctx.body.password === admin.password) {
        session.username = 'admin'
        session.grade = 'admin'
      } else {
        for (let user of userList) {
          if (ctx.body.username === user.username && ctx.body.password === user.password) {
            session.username = user.username
            session.grade = 'user'
            break
          }
        }
      }

      if (session.grade) {
        session.token = token_gen()
        sessions.push(session)
        ctx.body = {
          token: session.token
        }
        return
      }
    }
    ctx.body = {
      errorMsg: "Username or password invalid!"
    }
  } else {
    next()
  }
})

// guest redirect
app.use(async (ctx, next) => {
  if (!ctx.userGrade) {
    ctx.response.status = 401
    ctx.body = {
      errorMsg: "Please login first."
    }
  } else {
    next()
  }
})


app.use(async ctx => {
  if (ctx.req.url === '/admin') {
    if (ctx.userGrade === 'admin') {
      ctx.body = {
        status: "Admin"
      }
    } else {
      ctx.response.status = 401
      ctx.body = {
        errorMsg: "Unauthorized!"
      }
    }
  } else {
    ctx.body = {
      status: "Guest"
    }
  }
});

app.listen(3000);
