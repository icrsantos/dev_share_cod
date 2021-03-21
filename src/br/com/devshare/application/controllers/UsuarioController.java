package application.controllers;

import application.dao.UsuarioDao;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import application.dao.entidades.Usuario;

import java.util.Date;

@Controller
@RequestMapping(path="/usuario")
public class UsuarioController {
    @Autowired
    private UsuarioDao usuarioDao;

    @PostMapping(path="/adicionar") // Map ONLY POST Requests
    public @ResponseBody String addNewUser (@RequestParam String nome
            , @RequestParam String email) {
        Usuario n = new Usuario();
        n.setNome(nome);
        n.setEmail(email);
        usuarioDao.save(n);
        return n.toString();
    }

    @GetMapping(path="/buscar")
    public @ResponseBody Iterable<Usuario> getAllUsers() {
        return usuarioDao.findAll();
    }
}