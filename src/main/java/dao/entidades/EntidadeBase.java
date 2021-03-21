package dao.entidades;

import javax.persistence.*;
import java.io.Serializable;
import java.util.Date;

@MappedSuperclass
public abstract class EntidadeBase implements Serializable {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "ID")
    private Integer id;

    @Column(name = "DataAlteracao")
    private Date dataAlteracao;

    public EntidadeBase() {
    }

    public EntidadeBase(Integer id) {
        this.id = id;
    }

    public Integer getId() { return id; }
    public void setId(Integer id) { this.id = id; }

    public Date getDataAlteracao() { return dataAlteracao; }
    public void setDataAlteracao(Date dataAlteracao) { this.dataAlteracao = dataAlteracao;}


    @Override
    public int hashCode() {
        if (id != null)
            return id.hashCode();
        return super.hashCode();
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        EntidadeBase other = (EntidadeBase) obj;
        if (id == null) {
            return other.id == null;
        } else return id.equals(other.id);
    }
}
